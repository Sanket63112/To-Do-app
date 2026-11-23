import smtplib, ssl


def send_mail(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'sanket.sakharenitk@gmail.com'
    password = 'jhkmbplfacgpxkaz'

    receiver = 'sanket.sakhare2004@gmail.com'

    subject = "Today's news"
    body = (
        f"Subject :{subject}\n"
        f'From :{username}\n'
        f'To : {receiver}\n'
        f"MIME-Version: 1.0\n"
        f"Content-Type: text/plain; charset=utf-8\n"
        f"\n"  # <-- blank line separates headers from body
        f"{message}"

    )

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, body.encode('utf-8'))
