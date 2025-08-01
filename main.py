from stats import count_words, count_letters, sort_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        
        return file_contents
    
def print_report(book_location, word_count, letter_list):
   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {book_location}...")
   print("----------- Word Count ----------")
   print(f"Found {word_count} total words")
   print("--------- Character Count -------")
   for item in letter_list:
       print(f"{item[0]}: {item[1]}")
   print("============= END ===============")
   
def main():
    
    if len(sys.argv) == 2:
        book_location = sys.argv[1]
        
        book_text = get_book_text(book_location)
        
        word_count = count_words(book_text)
        
        letter_list = sort_list(count_letters(book_text))
        
        print_report(book_location, word_count, letter_list)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)    
    

if __name__ == "__main__":
    main()