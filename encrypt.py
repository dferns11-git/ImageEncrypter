#try block to handle the exception
try:

    #Path to file inputted by user
    path = input(r'Enter path of image: ')

    #Key which will be used to encrypt the image
    key = int(input('Enter the key for encryption of the image: '))

    #Printing path for testing
    # print('The path of the file: ', path)
    # print('The value of the key: ', key)

    #Open the image file
    f = open(path, 'rb')

    #Read the image file and store in image variable
    image = f.read()
    f.close()

    #Making use of the bytearray function to convert image into mutable sequence of bytes
    #This helps perform the XOR operation since the image data is in numeric form
    image = bytearray(image)

    #For loop to peform XOR operation on every byte of data in th array
    for index, values in enumerate(image):
        image[index] = values ^ key

    #Open the file
    f = open(path, 'wb')

    #Write into the file the encrypted data.
    f.write(image)
    f.close()
    print('Encryption done....')

#Exception handler for erros
except Exception:
    print('Error caught: ', Exception.__name__)