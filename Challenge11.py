rhyme = input("Enter first line of a rhyme: ").strip()
print(f"The length of the rhyme is {len(rhyme)} characters.")

start = int(input("Enter a start number: ").strip())
end = int(input("Enter an end number: ").strip())

print(f"The selected section of text is: {rhyme[start:end]}")