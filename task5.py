import string

def validation():

    ascii=string.ascii_letters
    digits=set(string.digits)
    punctuations=set(string.punctuation)
    whitespace=string.whitespace
    printable=string.printable

    data = {
        "ელ-ფოსტა": "useruser@gmail.com",
        "ზედმეტსახელი": "uu-coder8",
        "პაროლი": "12345678"
    }

    print(f"ელ-ფოსტა : {data['ელ-ფოსტა']}")
    print(f"ზედმეტსახელი : {data['ზედმეტსახელი']}")
    print(f"პაროლი : {data['პაროლი']}")
    
    while True:
        name=input("Enter your name or Exit : ").strip()

        if name.lower()=='exit':
            break

        if not name:
            print("შეიყვანეთ სახელი")
            continue

        if set(name)&set(digits):
            print("შემოყვანილია რიცხვითი მნიშვნელობა, შემოიტანეთ მხოლოდ string პატარა რეგისტრში")

        if set(name)&set(punctuations):
            print("შემოყვანილია სიმბოლო, შემოიტანეთ მხოლოდ string პატარა რეგისტრში")

        if set(name)&set(whitespace):
            print("შემოყვანილია სფეისი, შემოიტანეთ მხოლოდ string პატარა რეგისტრში")

        if not all(ch in printable for ch in name):
            print('შემოიყვანეთ მხოლოდ ლათინური ასოები')


        if all(ch in ascii for ch in name):
            data['სახელი'] = name.lower().capitalize()
            print('დარეგისტრირდა მომხმარებელი')
            for key,value in data.items():
                print(key, " : ", value)
            break


validation()