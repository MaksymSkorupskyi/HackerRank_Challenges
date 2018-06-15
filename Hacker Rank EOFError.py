while True:
  try:
    value = input()
    do_stuff(value) # next line was found
  except (EOFError):
    break #end of file reached


while True:
    try:
        query.append(input()) # next line was found
    except (EOFError):
        break #end of file reached