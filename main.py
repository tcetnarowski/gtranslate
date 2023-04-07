from google.cloud import translate_v3

project_id = 'projects/testproject-123456'

def translate_text(text, target_lang):
    client = translate_v3.TranslationServiceClient()
    request = translate_v3.TranslateTextRequest(
        contents=[text],
        target_language_code=target_lang,
        parent=project_id
    )
    response = client.translate_text(request=request)
    print(response)

translate_text('hello world', 'PL')
