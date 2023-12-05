import requests 
import json


def ocr_space_file(filename, overlay=True, api_key='K84842733188957', language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               "OCREngine": 2,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()

def OCR_results(fileName):
    test_file_response = ocr_space_file(filename=fileName)

    test_file_json = json.loads(test_file_response)
    print(test_file_json)
    
    # Check if there are ParsedResults and TextOverlay in the response
    if "ParsedResults" in test_file_json and test_file_json["ParsedResults"]:
        word_texts = []

        for line in test_file_json["ParsedResults"][0].get("TextOverlay", {}).get("Lines", []):
            for word in line.get("Words", []):
                word_texts.append(word.get("WordText", ""))

        # Printing the extracted WordText values
        print(word_texts)
        return word_texts
    else:
        print("Error in OCR processing. Check the response for details.")
        return None
