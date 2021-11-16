from twilio.rest import Client

account_sid = 'AC60ee84f4d34b723d7b0df4918696abca' #account sid 입력
auth_token = '181df32dcc0205ea445ff0d438b0f2a9' # auth token - show 눌러 확인 후 입력

to = ['+821039064638']

client = Client(account_sid, auth_token)

for i in to:
    message = client.messages.create(
        from_ = '+13187661738', #trial number 받기 눌러서 확인 후 입력
        body = '보호 대상에게 보이스피싱 의심 전화가 있었습니다.', #보낼 문자 내용
        to = i
    )

print(message.sid)
