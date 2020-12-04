class ChessPieces:
    def __init__(self, color, startRow, startFile):
        self.color = color
        self.exists = True
        self.rowPosition = startRow
        self.filePosition = startFile

    def movePiece(self, newRow, newFile):
        pass

    def isAttacking(self, chessPiece):
        pass

    def onBoard(self, row, file):
        if(row < 8 and row >= 0 and file < 8 and file >= 0):
            return True
        else:
            return False

    def getRow(self):
        return self.rowPosition

    def getFile(self):
        return self.filePosition

    def getColor(self):
        return self.color

    def doesExist(self):
        return self.exists


class King(ChessPieces):
    def movePiece(self, newRow, newFile):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if(filePosition + i == newFile and rowPosition + j == newRow):
                    rowPosition = newRow
                    filePosition = newFile
                    return True
        return False

    def isAttacking(self, chessPiece):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if(self.filePosition + i == chessPiece.getFile() and self.rowPosition + j == chessPiece.getRow()):
                    return True
        return False


class Queen(ChessPieces):
    def movePiece(self, newRow, newFile):
        # if self has same row or column as q, self is attacking q
        if (rowPosition == newRow or filePosition == newFile):
            rowPosition = newRow
            filePosition = newFile
            return True
        # if self is on same diagonal as q, this is attack. we use absolute values to determine diagonal
        elif(abs(rowPosition - newRow) == abs(filePosition - newFile)):
            rowPosition = newRow
            filePosition = newFile
            return True
        else:
            return False  # self is not attacking q

    def isAttacking(self, chessPiece):
        newRow = chessPiece.getRow()
        newFile = chessPiece.getFile()
        # if self has same row or column as q, self is attacking q
        if (rowPosition == newRow or filePosition == newFile):
            rowPosition = newRow
            filePosition = newFile
            return True
        # if self is on same diagonal as q, this is attack. we use absolute values to determine diagonal
        elif(abs(rowPosition - newRow) == abs(filePosition - newFile)):
            rowPosition = newRow
            filePosition = newFile
            return True
        else:
            return False  # self is not attacking q


class Knight(ChessPieces):
    def movePiece(self, newRow, newFile):
        # possible attack row positions
        attackRow = [-1, 1, -1, 1, -2, -2, 2, 2]
        # possible attack col positions
        attackCol = [-2, -2, 2, 2, -1, 1, -1, 1]

        for i in range(8):
            if(rowPosition + attackRow[i] == newRow and filePosition + attackCol[i] == newFile):
                rowPosition = newRow
                filePosition = newFile
                return True

        return False

    def isAttacking(self, chessPiece):
        # possible attack row positions
        attackRow = [-1, 1, -1, 1, -2, -2, 2, 2]
        # possible attack col positions
        attackCol = [-2, -2, 2, 2, -1, 1, -1, 1]

        for i in range(8):
            if(self.rowPosition + attackRow[i] == chessPiece.getRow() and self.filePosition + attackCol[i] == chessPiece.getFile()):
                return True

        return False


class Pawn(ChessPieces):
    def movePiece(self, newRow, newFile):
        if(self.color == "white" and rowPosition + 1 == newRow):
            rowPosition = newRow
            self.filePosition = newFile
            return True
        elif(self.color == "black" and rowPosition - 1 == newRow):
            rowPosition = newRow
            self.filePosition = newFile
            return True
        else:
            return False

    def isAttacking(self, chessPiece):
        pieceFile = chessPiece.getFile()
        pieceRow = chessPiece.getRow()
        if(self.color == "white" and abs(self.filePosition - pieceFile) == 1 and self.rowPosition + 1 == pieceRow):
            return True
        elif(self.color == "black" and abs(self.filePosition - pieceFile) == 1 and self.rowPosition - 1 == pieceRow):
            return True
        else:
            return False


class Bishop(ChessPieces):
    def movePiece(self, newRow, newFile):
        # if self is on same diagonal as q, this is attack. we use absolute values to determine diagonal
        if (abs(rowPosition - newRow) == abs(filePosition - newFile)):
            rowPosition = newRow
            filePosition = newFile
            return True
        else:
            return False

    def isAttacking(self, chessPiece):
        # if self is on same diagonal as q, this is attack. we use absolute values to determine diagonal
        if (abs(self.rowPosition - chessPiece.getRow()) == abs(self.filePosition - chessPiece.getFile())):
            return True
        else:
            return False


class Rook(ChessPieces):
    def movePiece(self, newRow, newFile):
        if (rowPosition == newRow or filePosition == newFile):
            rowPosition = newRow
            filePosition = newFile
            return True
        else:
            return False

    def isAttacking(self, chessPiece):
        if (self.rowPosition == chessPiece.getRow() or self.filePosition == chessPiece.getFile()):
            return True
        else:
            return False
