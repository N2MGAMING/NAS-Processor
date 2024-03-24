$ Adding the value in AX and BX (the result is in CX):
$	STO 0001 DX
$	CC
$--------------------------------------------------
$ Subtracting the value in BX from AX (the result is in CX):
$	STO 0010 DX
$	CC
$--------------------------------------------------
$ 								   (if ZEROFLAG = 0 and carry = 0 then AX = BX  )
$ Comparing the value in AX and BX (if ZEROFLAG = 1 and carry = -1 then AX < BX )
$ 							 	   (if ZEROFLAG = 1 and carry = 0 then AX > BX	)
$	STO 0011 DX
$	CC
$--------------------------------------------------
$ Clearing all the registers, the ZEROFLAG and the carry value:
$	STO 0000 DX
$	CC
$