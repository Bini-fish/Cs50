from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self.name = name
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("Helvetica", "B", size=50)
        self._pdf.cell(0, 50, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')
        self._pdf.image("shirtificate.png", w=self._pdf.epw, keep_aspect_ratio=True)
        # shirt text
        self._pdf.set_font("Times",size=30)
        self._pdf.set_text_color(255,255,255)
        self._pdf.text(x=48, y= 120,text=f"{name} took CS50")
        

        self._pdf.output("shirtificate.pdf")



def main():
    name = input("Name: ")
    pdf = PDF(name)
    



if __name__ == "__main__":
    main()