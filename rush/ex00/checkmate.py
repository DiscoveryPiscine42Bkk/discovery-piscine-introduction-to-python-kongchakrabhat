#ใช้เก็บตำแหน่งของ King (self.king), หมากรุกตัวอื่นๆ (self.pieces), และขนาดกระดาน (self.board_size)
class ChessPieces:
	def __init__(self, array):
		self.king = []
		self.pieces = []
		self.board_size = len(array)
#รับ board เป็น string ที่แทนแต่ละแถวคั่นด้วยเว้นวรรค เเละ ตรวจสอบว่ามี King แค่ 1 ตัว และกระดานเป็นสี่เหลี่ยมจัตุรัส
def checkmate(board):
	try:
		array = board.split()
		if board.count("K") != 1:
			return print("Error")
		for row in array:
			if len(row) != len(array):
				return print("Error")
#สร้างออบเจกต์ ChessPieces และบันทึกตำแหน่งของ King และหมากรุกตัวอื่น
		Chess = ChessPieces(array)
		for row in range(len(array)):
			for col in range(len(array[0])):
				if array[row][col] == "K":
					Chess.king = [row, col]
				elif array[row][col] in {"P", "R", "B", "Q"}:
					Chess.pieces.append([row, col])
#เรียกฟังก์ชัน check_all() เพื่อตรวจสอบว่า King โดนโจมตีหรือไม่ ถ้าใช่: แสดง "Success" ถ้าไม่ใช่: แสดง "Fail"		
		if check_all(array, Chess) == True:
			print("Success")
		else:
			print("Fail")
#ถ้ามีข้อผิดพลาด: แสดง "Error with exception"			
	except:
		 print("Error with exception")
#เช็คว่าหมากรุกตัวไหนโจมตี King ได้หรือเปล่า
def check_all(array, Chess):
	for row in range(len(array)):
		for col in range(len(array[0])):
			if array[row][col] == "P":
				if check_pawns(Chess, row, col) == True:
					return True
			elif array[row][col] == "R":
				if check_rooks(Chess, row, col) == True:
					return True
			elif array[row][col] == "B":
				if check_bishops(Chess, row, col) == True:
					return True
			elif array[row][col] == "Q":
				if check_queens(Chess, row, col) == True:
					return True
#Pawn โจมตีแนวทแยงหน้า (ขึ้นบนซ้าย/ขวา) เท่านั้น
def check_pawns(Chess, row, col):
	if [row - 1, col - 1] == Chess.king:
		return True
	elif [row - 1, col + 1] == Chess.king:
		return True
	return False
#Rook โจมตีแนวตรง (ขึ้น/ลง/ซ้าย/ขวา) เท่านั้น
def check_rooks(Chess, row, col):
	for direction in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
		if walk_to_king(direction[0], direction[1], Chess, row, col) == True:
			return True
	return False
#Bishop โจมตีแนวทแยง (ขึ้นบนซ้าย/ขวา, ลงล่างซ้าย/ขวา) เท่านั้น
def check_bishops(Chess, row, col):
	for direction in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
		if walk_to_king(direction[0], direction[1], Chess, row, col) == True:
			return True
	return False
#Queen โจมตีได้ทั้งแนวตรงและแนวทแยง (รวมกันของ Rook และ Bishop)
def check_queens(Chess, row, col):
	if check_rooks(Chess, row, col) == True:
		return True
	elif check_bishops(Chess, row, col) == True:
		return True
	return False
#ฟังก์ชัน walk_to_king ใช้เดินตามทิศทางที่กำหนด (dir_row, dir_col) จนกว่าจะเจอ King หรือเจอหมากรุกตัวอื่น
def walk_to_king(dir_row, dir_col, Chess, row, col):
	step = 1
	while step < Chess.board_size:
		move_row = row + (dir_row * step)
		move_col = col + (dir_col * step)
		if not (0 <= move_row < Chess.board_size and 0 <= move_col < Chess.board_size):
			return False
		if [move_row, move_col] == Chess.king:
			return True
		elif [move_row, move_col] in Chess.pieces:
			return False
		step = step + 1
	return False