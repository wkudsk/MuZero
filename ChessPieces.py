class ChessPieces:
    def __init__(self, color, startRow, startFile):
        self.color = color
        self.exists = True
        self.rowPosition = startRow
        self.filePosition = startFile

    def movePiece(self, newRow, newFile):
        pass

    def isBlockedBy(self, board, newRow, newFile):
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
    def __init__(self, color, startRow, startFile):
        super().__init__(color, startRow, startFile)
        self.pieceCode = ""
        if(self.getColor() == "white"):
            self.pieceCode = "WK"
        else:
            self.pieceCode = "BK"

    def movePiece(self, newRow, newFile):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if(self.filePosition + i == newFile and self.rowPosition + j == newRow):
                    self.rowPosition = newRow
                    self.filePosition = newFile
                    return True
        return False

    def castle(self, newRow, newFile):
        pass

    def isAttacking(self, chessPiece):
        if(chessPiece == None):
            return False
        elif(chessPiece.getColor() == self.color):
            return False
        for i in range(-1, 2):
            for j in range(-1, 2):
                if(self.filePosition + i == chessPiece.getFile() and self.rowPosition + j == chessPiece.getRow()):
                    return True
        return False

    def isBlocked(self, board, newRow, newFile):
        if(not (board[newRow][newFile] == None) and board[newRow][newFile].getColor() == self.color):
            return False
        return True

    def isInCheckMate(self, board):
        for row in board:
            for piece in row:
                if((not piece == None) and (not piece.getColor() == self.color) and piece.isAttacking(self)):
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if(board[i][j] == None):
                                return False
                    return True

    def getPieceCode(self):
        return self.pieceCode


class Queen(ChessPieces):
    def __init__(self, color, startRow, startFile):
        super().__init__(color, startRow, startFile)
        self.pieceCode = ""
        if(self.getColor() == "white"):
            self.pieceCode = "WQ"
        else:
            self.pieceCode = "BQ"

    def movePiece(self, newRow, newFile):
        # if self has same row or column as q, self is attacking q
        if (self.rowPosition == newRow or self.filePosition == newFile):
            self.rowPosition = newRow
            self.filePosition = newFile
            return True
        # if self is on same diagonal as q, this is attack. we use absolute values to determine diagonal
        elif(abs(self.rowPosition - newRow) == abs(self.filePosition - newFile)):
            self.rowPosition = newRow
            self.filePosition = newFile
            return True
        else:
            return False  # self is not attacking q

    def isAttacking(self, chessPiece):
        if(chessPiece == None):
            return False
        elif(chessPiece.getColor() == self.color):
            return False
        newRow = chessPiece.getRow()
        newFile = chessPiece.getFile()
        # if self has same row or column as q, self is attacking q
        if (self.rowPosition == newRow or self.filePosition == newFile):
            self.rowPosition = newRow
            self.filePosition = newFile
            return True
        # if self is on same diagonal as q, this is attack. we use absolute values to determine diagonal
        elif(abs(self.rowPosition - newRow) == abs(self.filePosition - newFile)):
            self.rowPosition = newRow
            self.filePosition = newFile
            return True
        else:
            return False  # self is not attacking q

    def isBlocked(self, board, newRow, newFile):
        if(not (board[newRow][newFile] == None) and board[newRow][newFile].getColor() == self.color):
            return False

        if(newRow == self.rowPosition):
            unitVector = int((newFile-self.filePosition) /
                             abs(newFile-self.filePosition))
            for i in range(self.filePosition + unitVector, newFile, unitVector):
                if(not board[newRow][i] == None):
                    return False
        elif(newFile == self.filePosition):
            unitVector = (int((newRow-self.rowPosition) /
                              abs(newRow-self.rowPosition)))
            for i in range(self.rowPosition + unitVector, newRow, unitVector):
                if(not board[i][newFile] == None):
                    return False
        else:
            unitVectorX = int((newRow-self.rowPosition) /
                              abs(newRow-self.rowPosition))
            unitVectorY = int((newFile-self.filePosition) /
                              abs(newFile-self.filePosition))
            if(not (board[newRow][newFile] == None) and board[newRow][newFile].getColor() == self.color):
                return True
            j = self.filePosition + unitVectorY
            for i in range(self.rowPosition + unitVectorX, newRow, unitVectorX):
                if(not board[i][j] == None):
                    print("Blocked by: %d %d" %
                          (i, j))
                    return False
                j += unitVectorY

        return True

    def getPieceCode(self):
        return self.pieceCode


class Knight(ChessPieces):
    def __init__(self, color, startRow, startFile):
        super().__init__(color, startRow, startFile)
        self.pieceCode = ""
        if(self.getColor() == "white"):
            self.pieceCode = "WN"
        else:
            self.pieceCode = "BN"

    def movePiece(self, newRow, newFile):
        # possible attack row positions
        attackRow = [-1, 1, -1, 1, -2, -2, 2, 2]
        # possible attack col positions
        attackCol = [-2, -2, 2, 2, -1, 1, -1, 1]

        for i in range(8):
            if(self.rowPosition + attackRow[i] == newRow and self.filePosition + attackCol[i] == newFile):
                self.rowPosition = newRow
                self.filePosition = newFile
                return True

        return False

    def isAttacking(self, chessPiece):
        if(chessPiece == None):
            return False
        elif(chessPiece.getColor() == self.color):
            return False
        # possible attack row positions
        attackRow = [-1, 1, -1, 1, -2, -2, 2, 2]
        # possible attack col positions
        attackCol = [-2, -2, 2, 2, -1, 1, -1, 1]

        for i in range(8):
            if(self.rowPosition + attackRow[i] == chessPiece.getRow() and self.filePosition + attackCol[i] == chessPiece.getFile()):
                return True

        return False

    def isBlocked(self, board, newRow, newFile):
        if(not (board[newRow][newFile] == None) and board[newRow][newFile].getColor() == self.color):
            return False

    def getPieceCode(self):
        return self.pieceCode


class Pawn(ChessPieces):
    def __init__(self, color, startRow, startFile):
        super().__init__(color, startRow, startFile)
        self.pieceCode = ""
        if(self.getColor() == "white"):
            self.pieceCode = "WP"
        else:
            self.pieceCode = "BP"

    def movePiece(self, newRow, newFile):
        if(abs(self.filePosition - newFile) > 0):
            return False
        elif(self.color == "white" and self.rowPosition - 1 == newRow):
            self.rowPosition = newRow
            self.filePosition = newFile
            return True
        elif(self.color == "white" and self.rowPosition == 6 and self.rowPosition - 2 == newRow):
            self.rowPosition = newRow
            self.filePosition = newFile
            return True
        elif(self.color == "black" and self.rowPosition + 1 == newRow):
            self.rowPosition = newRow
            self.filePosition = newFile
            return True
        elif(self.color == "black" and self.rowPosition == 1 and self.rowPosition + 2 == newRow):
            self.rowPosition = newRow
            self.filePosition = newFile
            return True
        else:
            return False

    def isAttacking(self, chessPiece):
        if(chessPiece == None):
            return False
        elif(chessPiece.getColor() == self.color):
            return False
        pieceFile = chessPiece.getFile()
        pieceRow = chessPiece.getRow()
        if(self.color == "white" and abs(self.filePosition - pieceFile) == 1 and self.rowPosition - 1 == pieceRow and chessPiece.getColor() == "black"):
            return True
        elif(self.color == "black" and abs(self.filePosition - pieceFile) == 1 and self.rowPosition + 1 == pieceRow and chessPiece.getColor() == "white"):
            return True
        else:
            return False

    def isBlockedBy(self, chessPiece):
        if(chessPiece == None):
            return False
        pieceRow = chessPiece.getRow()
        if(chessPiece.getColor() == self.color):
            return True
        elif(self.color == "white" and self.rowPosition - 1 == pieceRow):
            return True
        elif(self.color == "white" and self.rowPosition == 6 and self.rowPosition - 2 == pieceRow):
            return True
        elif(self.color == "black" and self.rowPosition + 1 == pieceRow):
            return True
        elif(self.color == "black" and self.rowPosition == 1 and self.rowPosition + 2 == pieceRow):
            return True
        else:
            return False

    def isBlocked(self, board, newRow, newFile):
        if(not (board[newRow][newFile] == None) and board[newRow][newFile].getColor() == self.color):
            return False
        return True

    def getPieceCode(self):
        return self.pieceCode


class Bishop(ChessPieces):
    def __init__(self, color, startRow, startFile):
        super().__init__(color, startRow, startFile)
        self.pieceCode = ""
        if(self.getColor() == "white"):
            self.pieceCode = "WB"
        else:
            self.pieceCode = "BB"

    def movePiece(self, newRow, newFile):
        # if self is on same diagonal as q, this is attack. we use absolute values to determine diagonal
        if (abs(self.rowPosition - newRow) == abs(self.filePosition - newFile)):
            self.rowPosition = newRow
            self.filePosition = newFile
            return True
        else:
            return False

    def isAttacking(self, chessPiece):
        if(chessPiece == None):
            return False
        elif(chessPiece.getColor() == self.color):
            return False
        # if self is on same diagonal as q, this is attack. we use absolute values to determine diagonal
        if (abs(self.rowPosition - chessPiece.getRow()) == abs(self.filePosition - chessPiece.getFile())):
            return True
        else:
            return False

    def isBlocked(self, board, newRow, newFile):
        unitVectorX = int((newRow-self.rowPosition) /
                          abs(newRow-self.rowPosition))
        unitVectorY = int((newFile-self.filePosition) /
                          abs(newFile-self.filePosition))
        if(not (board[newRow][newFile] == None) and board[newRow][newFile].getColor() == self.color):
            return True
        j = self.filePosition + unitVectorY
        for i in range(self.rowPosition + unitVectorX, newRow, unitVectorX):
            if(not board[i][j] == None):
                print("Blocked by: %d %d" %
                      (i, j))
                return False
            j += unitVectorY

        return True

    def getPieceCode(self):
        return self.pieceCode


class Rook(ChessPieces):
    def __init__(self, color, startRow, startFile):
        super().__init__(color, startRow, startFile)
        self.pieceCode = ""
        if(self.getColor() == "white"):
            self.pieceCode = "WR"
        else:
            self.pieceCode = "BR"

    def movePiece(self, newRow, newFile):
        if (self.rowPosition == newRow or self.filePosition == newFile):
            self.rowPosition = newRow
            self.filePosition = newFile
            return True
        else:
            return False

    def isAttacking(self, chessPiece):
        if(chessPiece == None):
            return False
        elif(chessPiece.getColor() == self.color):
            return False
        if (self.rowPosition == chessPiece.getRow() or self.filePosition == chessPiece.getFile()):
            return True
        else:
            return False

    def isBlocked(self, board, newRow, newFile):
        if(not (board[newRow][newFile] == None) and board[newRow][newFile].getColor() == self.color):
            return False

        if(newRow == self.rowPosition):
            unitVector = int((newFile-self.filePosition) /
                             abs(newFile-self.filePosition))
            for i in range(self.filePosition + unitVector, newFile, unitVector):
                if(not board[newRow][i] == None):
                    return False
        elif(newFile == self.filePosition):
            unitVector = (int((newRow-self.rowPosition) /
                              abs(newRow-self.rowPosition)))
            for i in range(self.rowPosition + unitVector, newRow, unitVector):
                if(not board[i][newFile] == None):
                    return False
        return True

    def getPieceCode(self):
        return self.pieceCode
