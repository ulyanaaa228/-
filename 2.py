
def handler(event, context):
    """
    Entry-point for Serverless Function.
    :param event: request payload.
    :param context: information about current execution context.
    :return: response to be serialized as JSON.
    """
    keyboardFakts = [
                        {
                            "title": "О программировании",
                            "payload": 'buttonProgs',
                            "hide": 'true'
                        },
                        {
                            "title": "О рисовании",
                            "payload": 'buttonPaints',
                            "hide": 'true'
                        },
                        {
                            "title": "О кулинарии",
                            "payload": 'buttonBakers',
                            "hide": 'true'
                        },
                        {
                            "title": "О гитаре",
                            "payload": 'buttonGitars',
                            "hide": 'true'
                        },
                        {
                            "title": "Главное меню",
                            "payload": 'buttonMenu',
                            "hide": 'true'
                        }
                    ]
    keyboardInfo =  [
                        {
                            "title": "Откуда навык берет информацию",
                            "payload": 'buttonInfoFrom',
                            "hide": 'true'
                        },
                        {
                            "title": "Чему сейчас можно научиться",
                            "payload": 'buttonWhatCanLearn',
                            "hide": 'true'
                        },
                        {
                            "title": "Связь с разработчиками",
                            "payload": 'buttonCreaters',
                            "hide": 'true'
                        }
                    ]
    keyboardMenu = [
                        {
                            "title": "Интересные факты",
                            "payload": 'buttonFakts',
                            "hide": 'true'
                        },
                        {
                            "title": "Информация",
                            "payload": 'buttonInfo',
                            "hide": 'true'
                        }
                    ]
    text = 'Добро пожаловать в "Шаг за шагом"! Независимо от того, являетесь ли Вы новичком или опытным учеником, моя миссия состоит в том, чтобы помочь Вам освоить новые навыки веселым и увлекательным способом. С моей помощью Вы сможете разбить сложные задачи на простые, понятные для выполнения шаги. От рисования и кулинарии до программирования и игре на гитаре - всему этому Вы можете научиться с помощью навыка "Шаг за шагом". Вместе мы будем изучать новые темы и полностью раскрывать Ваш потенциал.  Так давайте же начнем Ваш путь к успеху!\n\n\nЧем бы вы занялись в первую очередь?'
    if 'value' in event['state']['user']:
        state = event['state']['user']['value']
    else:
        state = 0
    if state == 0:
        return {
            'version': event['version'],
            'session': event['session'],
            'response': {
                # Respond with the original request or welcome the user if this is the beginning of the dialog and the request has not yet been made.
                'text': text,
                'buttons': keyboardMenu,
                # Don't finish the session after this response.
                
                'end_session': 'false'
            },
            "user_state_update": {
                "value": 2
            }
        }
    else:
        if 'request' in event and "payload" in event['request']:
            payload = event['request']["payload"]
        else:
            payload = None
        if payload == 'buttonMenu':
            return {
                'version': event['version'],
                'session': event['session'],
                'response': {
                    # Respond with the original request or welcome the user if this is the beginning of the dialog and the request has not yet been made.
                    'text': text,
                    'buttons': keyboardMenu,
                    # Don't finish the session after this response.
                    
                    'end_session': 'false'
                },
                "user_state_update": {
                    "value": 2
                }
            }
        elif state == 2 or payload == 'buttonFakts':
            text = "Факты о чем вы бы хотели узнать?"
            return {
                'version': event['version'],
                'session': event['session'],
                'response': {
                    # Respond with the original request or welcome the user if this is the beginning of the dialog and the request has not yet been made.
                    'text': text,
                    'buttons': keyboardFakts,
                    # Don't finish the session after this response.
                    'end_session': 'false'
                },
                "user_state_update": {
                        "value": 3
                    }
            }