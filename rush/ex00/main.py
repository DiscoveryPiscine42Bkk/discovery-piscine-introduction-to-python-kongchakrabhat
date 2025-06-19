#นำเข้าฟังก์ชัน checkmate จากโมดูลชื่อ checkmate
from checkmate import checkmate
#นิยามฟังก์ชันหลักชื่อ main ที่จะใช้ในการทำงานหลักของโปรแกรม
def main():
#นิยามตัวแปรชื่อ board ซึ่งเป็น string แบบหลายบรรทัด แทนกระดานหมากรุกขนาด 2x2
 board = """\
..
.K\
"""
 checkmate(board)
#ฟังก์ชัน main() ถูกรันเ 
if __name__ == "__main__":
 main()