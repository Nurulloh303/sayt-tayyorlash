from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.

def sinf(request: HttpRequest):
    return HttpResponse('<h2>Siz nechanchi sinfsiz iltimos tanlang</h2>'
                        '<select>'
                        '<option value="1">7-sinf</option>'
                        '<option value="2">8-sinf</option>'
                        '<option value="3">9-sinf</option>'
                        '</select>')

def bmw(request: HttpRequest):
    return HttpResponse('<a href="https://www.google.com/search?sca_esv=392931b93c8c4b33&sxsrf=AE3TifM9vnZzvIZkvbmpCaPbc21gQ5RjnA:1755315530985&udm=2&fbs=AIIjpHy3vMFde4-A-s4rkZ3m7V6OiDP_Mkp93blFcU-WdeYUQpMD3MmH-uIKRtMPEqU9UTjsGBeEBGZrz1vJhmlW14Ut6jLAki7br8xF-tiCL1ijbXL8ike9-FMO3T4H-36Josa9o5WXPQ2Gog0Ve3Nd7zDIJE2scjuBKUWTY2t2CfdHDABH9Ke6nOJC3_j1UFQDsRpzqx9X4VMUh8rQaBO5IU0gtTRdSZgMTOQJ4edfdUI2KSk7Mlw&q=bmw+m5+rasm&sa=X&ved=2ahUKEwjqwMX1s46PAxUpExAIHf6zCA0QtKgLegQIEBAB&biw=1536&bih=695&dpr=1.25">BMW M5 mashinasini rasmini korish uchun iltimos meni bosing</a>')


def mers(request: HttpRequest):
    return HttpResponse('<a href="https://www.google.com/search?q=mers+rasm&sca_esv=392931b93c8c4b33&udm=2&biw=1536&bih=816&sxsrf=AE3TifNzu8s4ujK3-g8D4T-szmlNjKKPWw%3A1755315533356&ei=Tf2faK6_FdWowPAP-bms4AY&ved=0ahUKEwjumdb2s46PAxVVFBAIHfkcC2wQ4dUDCBE&uact=5&oq=mers+rasm&gs_lp=EgNpbWciCW1lcnMgcmFzbTIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgQQABgeMgYQABgKGB4yBhAAGAUYHjIGEAAYBRgeMgYQABgFGB5IvTBQAFjHCXAAeACQAQCYAbwFoAGKGKoBCzItMS4xLjAuMy4xuAEDyAEA-AEBmAICoALZBMICBhAAGAcYHpgDAJIHBTItMS4xoAf7HLIHBTItMS4xuAfZBMIHAzQtMsgHOA&sclient=img">Mersades-Benz rasmini korish uchun meni bosing</a>')