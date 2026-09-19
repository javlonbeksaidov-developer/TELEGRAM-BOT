from googletrans import Translator

translator = Translator()


async def translate_to_eng(translator, text):
    result = await translator.translate(text=text, dest="en")
    return result.text


async def translate_eng_uz(translator, text):
    result = await translator.translate(text=text, dest="uz")
    return result.text


async def translate(text):
    async with Translator() as translator:
        detection = await translator.detect(text)
        if detection.lang == "uz":
            return await translate_to_eng(translator, text)
        elif detection.lang == "en":
            return await translate_eng_uz(translator, text)
        else:
            return await translate_to_eng(translator, text)
