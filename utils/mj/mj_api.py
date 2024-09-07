import discord
import requests


class SalaiApi:
    # [Token of Discord bot]
    DAVINCI_TOKEN:str = None
    # [Server id here]
    SERVER_ID:str = None
    # [Token of the Account from which you paid MidJourney ]
    SALAI_TOKEN:str = None
    # [Channel in which commands are sent]
    CHANNEL_ID:str = None
    # boolean
    USE_MESSAGED_CHANNEL:bool = False
    #don't edit the following variable
    MID_JOURNEY_ID:str = "936929561302675456"  #midjourney bot id
    targetID:str       = ""
    targetHash:str     = ""

    def __init__(s, davinci_token:str, server_id:str,salai_token:str, channel_id:str, use_messaged_channel:bool=False):
        s.DAVINCI_TOKEN=davinci_token
        s.SERVER_ID=server_id
        s.SALAI_TOKEN=salai_token
        s.CHANNEL_ID=channel_id
        s.USE_MESSAGED_CHANNEL=use_messaged_channel
        pass

    def PassPromptToSelfBot(s, prompt:str):
        payload = {
            "type":2,
            "application_id":"936929561302675456",
            "guild_id":s.SERVER_ID,
            "channel_id":s.CHANNEL_ID,
            "session_id":"2fb980f65e5c9a77c96ca01f2c242cf6",
            "data":{
                "version":"1077969938624553050",
                "id":"938956540159881230",
                "name":"imagine",
                "type":1,
                "options":[{"type":3,"name":"prompt","value":prompt}],
                "application_command":{
                    "id":"938956540159881230",
                    "application_id":"936929561302675456",
                    "version":"1077969938624553050",
                    "default_permission":True,
                    "default_member_permissions":None,
                    "type":1,"nsfw":False,"name":"imagine","description":"Create images with Midjourney",
                    "dm_permission":True,
                    "options":[{"type":3,"name":"prompt","description":"The prompt to imagine","required":True}]
                },
                "attachments":[]
            }
        }
        
        headers = {
            'authorization' : s.SALAI_TOKEN
        }
        
        response = requests.post("https://discord.com/api/v9/interactions",json = payload,headers = headers)
        return response
        
    def Upscale(s, index : int, messageId : str, messageHash : str):
        payload = {
            "type":3,
            "guild_id":s.SERVER_ID,
            "channel_id":s.CHANNEL_ID,
            "message_flags":0,
            "message_id": messageId,
            "application_id":"936929561302675456",
            "session_id":"45bc04dd4da37141a5f73dfbfaf5bdcf",
            "data":{
                "component_type":2,
                "custom_id":"MJ::JOB::upsample::{}::{}".format(index, messageHash)
            }
        }
        
        header = {
            'authorization' : s.SALAI_TOKEN
        }
        
        response = requests.post("https://discord.com/api/v9/interactions",json = payload, headers = header)
        return response
        
    def Variation(index : int,messageId : str, messageHash : str):
        payload = {
            "type":3,
            "guild_id":s.SERVER_ID,
            "channel_id": s.CHANNEL_ID,
            "message_flags":0,
            "message_id": messageId,
            "application_id": "936929561302675456",
            "session_id":"1f3dbdf09efdf93d81a3a6420882c92c",
            "data":{"component_type":2,"custom_id":"MJ::JOB::variation::{}::{}".format(index, messageHash)}
        }
        header = {
            'authorization' : s.SALAI_TOKEN
        }
        response = requests.post("https://discord.com/api/v9/interactions",
        json = payload, headers = header)
        return response
    
    def MaxUpscale(s, messageId : str, messageHash : str):        
        payload = {
            "type":3,
            "guild_id":s.SERVER_ID,
            "channel_id":s.CHANNEL_ID,
            "message_flags":0,
            "message_id": messageId,
            "application_id":"936929561302675456",
            "session_id":"1f3dbdf09efdf93d81a3a6420882c92c",
            "data":{
                "component_type":2,
                "custom_id":"MJ::JOB::upsample_max::1::{}::SOLO".format(messageHash)
            }
        }
         
        header = {
            'authorization' : s.SALAI_TOKEN
        }
        
        response = requests.post("https://discord.com/api/v9/interactions",json = payload, headers = header)
        return response
    
    
class DiscordBot:
    SALAI:SalaiApi = None
    bot = None
    def __init(s, davinci_token:str, server_id:str,salai_token:str, channel_id:str, use_messaged_channel:bool=False):
        s.SALAI=SalaiApi(davinci_token=davinci_token, server_id=server_id,salai_token=salai_token,channel_id=channel_id,use_messaged_channel=use_messaged_channel)
        s.bot = discord.bot(intents=discord.Intents.all())
        pass