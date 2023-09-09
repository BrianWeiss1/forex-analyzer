import re

def convert_dataset(dataset_file):
  """Converts the dataset in the specified file to an array in the specified format.

  Args:
    dataset_file: The path to the dataset file.

  Returns:
    An array of the converted dataset.
  """

  with open(dataset_file, "r") as f:
    dataset = f.read()

  # Split the dataset into lines.
  lines = dataset.split("\n")

  # Remove empty lines.
  lines = [line for line in lines if line]

  # Convert each line to an array.
  array = []
  for line in lines:
    array.append(re.split(" --> ", line.strip(' ')))

  # Return the array.
  for row in range(len(array)):
    array[row][2] = array[row][2].replace(",", "")
    # print(array[row][2])
  dataset = array
  # Get the value column.
  value_column = dataset[2]

  # Sort the dataset by the value column in descending order.
  dataset.sort(key=lambda x: float(x[2]), reverse=True)

  return dataset


def main():
  dataset_file = "documents/test.txt"

  # Convert the dataset to an array.
  array = convert_dataset(dataset_file)

  for i in range(len(array)):
    print("\n")
    print(str(i+1) + ":" + str(array[i][0]) + str(array[i][2]))

  # Print the array.
  print(array)


if __name__ == "__main__":
  main()
