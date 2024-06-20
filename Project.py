from PIL import Image, ImageDraw

def load_handwritten_letters():
    letters = {}
    for char in """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"#$%&'()*+,-./:;<>=?@[]\^_`}{|~""":
        if char == '"':
            letters[char] = Image.open("db.png").convert("RGBA")
        elif char == '*':
            letters[char] = Image.open("st.png").convert("RGBA")
        elif char == '.':
            letters[char] = Image.open("dot.png").convert("RGBA")
        elif char == '/':
            letters[char] = Image.open("sls.png").convert("RGBA")
        elif char == '$':
            letters[char] = Image.open("dl.png").convert("RGBA")
        elif char == '%':
            letters[char] = Image.open("perc.png").convert("RGBA")
        elif char == '-':
            letters[char] = Image.open("hy.png").convert("RGBA")
        elif char == ':':
            letters[char] = Image.open("semi.png").convert("RGBA")
        elif char == ';':
            letters[char] = Image.open("semi1.png").convert("RGBA")
        elif char == '<':
            letters[char] = Image.open("lesst.png").convert("RGBA")
        elif char == '>':
            letters[char] = Image.open("great.png").convert("RGBA")
        elif char == '=':
            letters[char] = Image.open("eq.png").convert("RGBA")
        elif char == '?':
            letters[char] = Image.open("qn.png").convert("RGBA")
        elif char == '@':
            letters[char] = Image.open("att.png").convert("RGBA")
        elif char == '[':
            letters[char] = Image.open("brr.png").convert("RGBA")
        elif char == ']':
            letters[char] = Image.open("brl.png").convert("RGBA")
        elif char == '\\':   #do // because \ yo ta escape charater ho ni ta
            letters[char] = Image.open("slsl.png").convert("RGBA")
        elif char == '^':
            letters[char] = Image.open("ttp.png").convert("RGBA")
        elif char == '_':
            letters[char] = Image.open("under.png").convert("RGBA")
        elif char == '`':
            letters[char] = Image.open("omg.png").convert("RGBA")
        elif char == '{':
            letters[char] = Image.open("crr.png").convert("RGBA")
        elif char == '|':
            letters[char] = Image.open("orr.png").convert("RGBA")
        elif char == '}':
            letters[char] = Image.open("crl.png").convert("RGBA")
        elif char == '~':
            letters[char] = Image.open("neq.png").convert("RGBA")
        
        
        else:
            try:
                letters[char] = Image.open(f"{char}.png").convert("RGBA")
            except FileNotFoundError:   
                print(f"Handwritten image for {char} not found.")

    return letters

def convert_to_handwritten(text, letters):

    paper = Image.open("copy1.jpg").convert("RGBA")
    paper_width, paper_height = paper.size 
    draw = ImageDraw.Draw(paper)

    x, y = 200,320 
    line_height = max(letters['A'].size[1], letters['a'].size[1]) + 15 

    for char in text:
        if char in letters:
            letter_img = letters[char]
            paper.paste(letter_img, (x, y), letter_img)
            x += letter_img.size[0] + 2
        elif char == ' ':
            x += 30  
        elif char == '\n':
            x = 200
            y += line_height

        if x >= paper_width - 50:
            x = 200
            y += line_height

    return paper

def main():
    letters = load_handwritten_letters()
    text = """ 
    Hello anurag!!!!. k xa? hello kx dfasdfasdfasd344
-- Deepak Thapa

    """
    handwritten_image = convert_to_handwritten(text, letters)
    handwritten_image.show() 

if __name__ == "__main__":
    main()
