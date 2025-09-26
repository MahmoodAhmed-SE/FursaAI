from playwright.sync_api import sync_playwright
import time, random, os, json

default_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/125.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }

URL = os.environ["URL"]
output_file = "jobs.json"

def main():
    if os.path.exists(output_file):
        with open(output_file, "r", encoding="utf-8") as f:
            try:
                jobs = json.load(f)
            except json.JSONDecodeError:
                jobs = []
    else:
        jobs = []

    with sync_playwright() as pw:
        browser = pw.chromium.launch_persistent_context(
            headless=False, user_data_dir="userdata"
        )
        page = browser.new_page()
        page.set_extra_http_headers(default_headers)
        
        page.goto(URL)

        for postElement in page.locator("div.elementor-post__card").all():
            title = postElement.locator("div.elementor-post__text").text_content()
            link = postElement.locator("a.elementor-post__thumbnail__link").get_attribute("href")
            if not link:
                continue
            
            new_page = browser.new_page()
            new_page.set_extra_http_headers(default_headers)
            time.sleep(random.random() * 3)

            new_page.goto(link)

            try:
                content = new_page.locator("div.entry-content.no-share div.content-inner")
                
                text_content = content.text_content()
                lastIndex = text_content.find("للتقديم اضغط هنا")
                if (lastIndex == -1):
                    raise ValueError(f"'للتقديم اضغط هنا' was not found in: {text_content}")
                
                text_content = text_content[:lastIndex]

                application_link_element = content.locator("a").first
                application_link = application_link_element.get_attribute("href")

                print(f"Title: {title}")
                print(f"URL: {link}")
                print("Application link:", application_link, "\n")
                print("Content:", text_content, "\n")
                
                jobs.append({
                        "title": title,
                        "url": link,
                        "application_link": application_link,
                        "content": text_content
                    })

                with open(output_file, "w", encoding="utf-8") as f:
                  try:
                      json.dump(
                          jobs,
                          f,
                          ensure_ascii=False,
                          indent=2
                      )
                  except Exception as e:
                      print(f"Failed to write content into jobs.json for {title}: {e}")
                      break
            except Exception as e:
                print(f"Failed to get content for {title}: {e}")
                break

            new_page.close()
        page.close()



if __name__ == "__main__":
  main()