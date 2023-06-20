from ascii_magic import AsciiArt

my_art = AsciiArt.from_image('Samantha.jpg')
my_art.to_html_file('index.html', columns=200)