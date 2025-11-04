from transformers import pipeline
import json

print("INFO: Loading the model...")

pipe = pipeline(
      "text-generation",
      model="Qwen/Qwen2.5-1.5B-Instruct",
      device_map="auto",
    )

print("INFO: Finished loading the model...")


def getJson(html_content: str) -> str:
    messages = [
        {
        "role": "system",
        "content": '''
            You are a precise and reliable job extractor.

            Your task is to analyze the provided HTML and extract all job postings as structured JSON objects.

            Output **only** a valid JSON array (no explanations, no Markdown, no HTML).  
            Each job must be a JSON object enclosed within `{}`, and all jobs must be separated by commas inside `[]`.

            Each object must include **exactly** the following 5 fields:
            - "company_name": string  
            - "job_title": string  
            - "job_description": string (rephrased clearly and concisely)  
            - "requirements": list of strings  
            - "application_link": string (or other contact info such as email or phone if no link exists)

            Rules:
            - Do not include any extra keys or text outside the JSON.
            - Combine multiple job listings into one JSON array.
            - Ensure the JSON is syntactically valid and well-formatted.
            - Always provide all the 5 fields, even if they are empty.

        ''',
        },
        {
            "role": "user",
            "content": f"{html_content}",
        }
    ]

    result = pipe(
        messages,
        max_new_tokens=2000,
        temperature=0.4,
        top_p=0.9,
        repetition_penalty=1.1,
    )


    return result[0]["generated_text"][len(result[0]["generated_text"]) - 1]['content']



html_content = '''
<p>أعلنت شركة إنسايت عن رغبتها بتعيين لديها :</p><ol class="wp-block-list"><li>محلل أمن المعلومات – المستوى 1 (L1) بالشروط التالية :</li></ol><p>. درجة البكالوريوس في الأمن السيبراني أو علوم الحاسوب أو مجال ذي صلة (أو خبرة معادلة).<br>. فهم أساسي لمفاهيم الشبكات (TCP/IP، DNS، إلخ).<br>. الإلمام بتقنيات الأمن مثل أنظمة إدارة المعلومات والأحداث الأمنية (SIEM)، الجدران النارية، EDR، مضادات الفيروسات.<br>. معرفة بأنواع التهديدات (البرمجيات الخبيثة، التصيد الاحتيالي، هجمات DDoS، إلخ).<br>. مهارات تحليلية واتصالية قوية.<br>. القدرة على العمل بنظام المناوبات على مدار الساعة طوال الأسبوع، بما في ذلك ليالي وعطلات نهاية الأسبوع.</p><div class="jeg_ad jeg_ad_article jnews_content_inline_ads  "><div class="ads-wrapper align-center "><div class="ads_shortcode"><div data-advads-trackid="8173914" data-advads-trackbid="1" class="advads-target" id="advads-3811756496"><a data-no-instant="1" href="https://www.whatsapp.com/channel/0029VaCw28WAO7RIwUkSNT0T" rel="noopener" class="a2t-link" target="_blank" aria-label="whats app channel ol"><img src="https://ol.om/wp-content/uploads/2025/06/Brown-Simple-Marketing-Solutions-LinkedIn-Banner.png" alt="" srcset="https://ol.om/wp-content/uploads/2025/06/Brown-Simple-Marketing-Solutions-LinkedIn-Banner.png 792w, https://ol.om/wp-content/uploads/2025/06/Brown-Simple-Marketing-Solutions-LinkedIn-Banner-300x75.png 300w, https://ol.om/wp-content/uploads/2025/06/Brown-Simple-Marketing-Solutions-LinkedIn-Banner-768x192.png 768w, https://ol.om/wp-content/uploads/2025/06/Brown-Simple-Marketing-Solutions-LinkedIn-Banner-750x188.png 750w" sizes="(max-width: 792px) 100vw, 792px" width="792" height="198" data-pin-no-hover="true"></a></div></div></div></div><p>. مراقبة التنبيهات والأحداث الأمنية باستخدام SIEM وأدوات أخرى.<br>. إجراء التقييم الأولي لتحديد خطورة ومصداقية التنبيهات.<br>. توثيق الحوادث وتصعيدها وفق الإجراءات والمعايير المحددة إلى محللي المستوى الثاني/الثالث.<br>. اتباع إجراءات التشغيل القياسية (SOPs) للكشف عن الحوادث والاستجابة لها.<br>. إجراء تحليل أساسي للتهديدات باستخدام مصادر استخبارات التهديدات ومطابقة مؤشرات الاختراق (IOC).<br>. الإبلاغ عن الإيجابيات الكاذبة وتحسين ضبط الكشف بالتعاون مع فريق الهندسة أو محللي المستوى الثاني.<br>. الحفاظ على توثيق دقيق وفي الوقت المناسب لجميع أنشطة SOC والتحقيقات في الحوادث.</p><p>المؤهلات المفضلة :</p><p>. شهادات أمنية مثل CompTIA Security+ أو CySA+ أو ما يعادلها.<br>. خبرة بأدوات مثل Splunk أو IBM QRadar أو Microsoft Sentinel.<br>. خبرة سابقة في التدريب أو 6-12 شهرًا في بيئة SOC أو الأمن السيبراني.</p><ol start="2" class="wp-block-list"><li>محلل أمن المعلومات – المستوى 2 بالشروط التالية :</li></ol><p>. درجة في الأمن السيبراني أو علوم الحاسوب.<br>. شهادة محلل SOC.<br>. شهادة متعامل مع الحوادث (Incident Handler).<br>. شهادة تحليل البرمجيات الخبيثة (Malware Analysis).<br>. خبرة في مهام مشابهة.<br>. معرفة متقدمة بلغات البرمجة وسينتاكسها.<br>. القدرة على كتابة تعليمات وإجراءات العمل.<br>. فهم قوي لتقنيات الهجوم والمعايير الأمنية مثل MITRE، Cyber Kill Chain، NIST، وأي إضافات أخرى تعتبر ميزة.<br>. خبرة من سنتين إلى خمس سنوات.<br>. مهارات تقديم العروض والتقارير.<br>. تحمل مسؤولية التحقيق في الحوادث، جمع الأدلة، التشخيص، الاسترداد، وإغلاق الحوادث.<br>. القدرة على إجراء تحليل البرمجيات الخبيثة والتحقيقات الجنائية الرقمية على أنظمة تشغيل متعددة.<br>. التنسيق مع العملاء و/أو الشركاء لوضع خطط العمل وحل المشكلات.<br>. إجراء تحليل سجلات غير متصل بالشبكة (offline log analysis).<br>. التمييز بين الإيجابيات الكاذبة والتهديدات الفعلية.<br>. إنشاء Playbooks وحالات الاستخدام (Use Cases) وتحسينها وضبطها.<br>. القدرة على العمل مع منصات أمنية سيبرانية متعددة.<br>. تحديد الإجراءات اللازمة لتحقيق النتائج المطلوبة، وتقديم التوصيات والتعديلات على سياسات وإجراءات القسم.<br>. إظهار الكفاءات الأساسية: العمل في عمليات الأمن، معرفة مراكز البيانات، التهديدات السيبرانية، وفهم حالات الاستخدام.<br>. فهم متقدم لأدوات وتقنيات الأمن مثل WAF، الجدران النارية، EDR، SIEM المتقدم، أجهزة التوجيه والمحولات، البروكسي، موازنات التحميل، بوابات البريد الإلكتروني، وغيرها.<br>. فهم والعمل مع فريق الاستجابة للحوادث (Incident Response).<br>. الإشراف على أدوات المراقبة الأمنية وتكوينها.<br>. تقديم قيادة مثالية في بيئة تحديّة ومجزية، والتأثير على المنظمة.<br>. فهم واستخدام على الأقل نظامي SIEM.<br>. القدرة على كتابة تعليمات وإجراءات العمل.<br>.؟تنفيذ تسليم واستلام المناوبة وفق الإجراءات.<br>. أداء جميع المهام وفق العمليات الداخلية بكفاءة وجودة عالية.<br>. اجتياز برامج التقييم الداخلي ومتطلبات تطوير المهارات.<br>. تنفيذ المهام التحليلية والتكتيكية في المواقف الصعبة.<br>. القدرة على الإشراف على فريق من المحللين.<br>. القدرة على العمل تحت ضغط عالٍ.</p><p>للتواصل وارسال السيرة الذاتية :</p><p>info@insight.om</p><p>لتصفح جديد الوظائف والتدريب <a href="https://ol.om/jobs">اضغط هنا </a></p><p>تابعنا على قناة الوظائف والأخبار العاجلة من خلال الرابط التالي ولا تنسَ تفعيل التنبيهات <a href="https://whatsapp.com/channel/0029VaCw28WAO7RIwUkSNT0T" target="_blank" rel="noopener">اضغط هنا </a></p>
'''


resp = getJson(html_content)

cleaned = resp.removeprefix("```json").removesuffix("```")

try:
    jobs = json.loads(cleaned)
    
except Exception as e:
    print(e)