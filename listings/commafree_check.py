__author__ = 'skumaran'

comma_free_words = []


def check_periodic(input_string):
  head = input_string[:len(input_string) / 2]
  tail = input_string[len(head):]
  return head == tail


def get_parts(input_string):
  parts = []
  for idx in range(len(input_string)):
    parts.append((input_string[:idx], input_string[idx:]))
  return parts


def any_starts_with(head):
  for word in comma_free_words:
    if word.startswith(head):
      return True
  return False


def any_ends_with(tail):
  for word in comma_free_words:
    if word.endswith(tail):
      return True
  return False


def check_comma_free(input_string):
  if check_periodic(input_string):
    print("input string is periodic, it cannot be commafree.")
    return
  if len(comma_free_words) == 0:
    comma_free_words.append(input_string)
  else:
    parts = get_parts(input_string)
    for head, tail in parts:
      if (any_starts_with(head) and any_ends_with(tail)) or (any_starts_with(tail) and any_ends_with(head)):
        print("%s|%s are part of the previous words." % (head, tail))
        return
    comma_free_words.append(input_string)

if __name__ == '__main__':
  while True:
    input_string = raw_input()
    if input_string == '':
      break
    if len(input_string) != 4:
      print("Please give a string of length 4.")
    else:
      check_comma_free(input_string)
  print("The total number of comma free words was %d " % len(comma_free_words))
