# this function compresses a given text file
def compress(file: str, encoding: str) -> str:
  # opens the file and store the raw binary data
  with open(file, 'rb') as f:
    raw_data: bytes = f.read()

  # decodes the raw binary data into a string
  data: str = raw_data.decode(encoding)

  compressed_data: list[tuple] = []
  multiplier: int = 1

  # groups characters together into tuples which are then appended into a list
  for n in range(len(data)-1):
    # checks if the next character is equal to the current one
    if data[n] == data[n+1]:
      # adds one to the multiplier
      multiplier += 1

    # checks if the next character is not equal to the current one
    elif data[n] != data[n+1]:
      # appends tuple to the list and resets multiplier back to one
      compressed_data.append(tuple([data[n], multiplier]))
      multiplier = 1

  # appends the final character
  compressed_data.append(tuple([data[-1], multiplier]))

  # splits the file's name and suffix
  substrings = file.split('.')
  # creates new file name based on original file's name
  newfile = f'compressed_{substrings[0]}_{substrings[1]}'

  # writes the new file
  with open(newfile, 'w') as f:
    f.write(str(compressed_data))

  # returns the name of the new file
  return newfile


# this function extracts the data from a previously text file previously compressed by this program
def extract(file: str, encoding: str) -> str:
  # opens the compressed file
  with open(file, 'r') as f:
    compressed_data = eval(f.read())
    
  data:str = ''

  # appends characters to a string
  for character,multiplier in compressed_data:
    # appends a character a specified amount to a string
    for _ in range(multiplier):
      data += character

  # encodes the string into raw binary data
  raw_data = data.encode(encoding)
  # splits the file's name and suffix
  substrings = file.split('_')
  # creates new file name based on original file's name
  newfile = f'uncompressed_{substrings[1]}.{substrings[2]}'

  # writes the new file
  with open(newfile, 'wb') as f:
    f.write(raw_data)

  # returns the name of the new file
  return newfile

def main():
  select = int(input('compress(1), extract(2), exit(3): '))
    
  try:	
    if select == 1:
      file = input('input filename: ')
      newfile = compress(file=file, encoding='utf-8')
      print(f'file successfully compressed as {newfile}\n')

    elif select == 2:
      file = input('input filename: ')
      newfile = extract(file=file, encoding='utf-8')
      print(f'file successfully extracted as {newfile}\n')

    elif select == 3:
      exit()

    else:
      print('invalid input\n')
    
  except Exception as e:
    print(e)

if __name__ == '__main__':
  main()
