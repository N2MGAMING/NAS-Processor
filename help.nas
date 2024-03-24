$--------------------------------------------------
$ To use decimal numbers add 'INT' in the start ex: INT3 = 0011
$-------------------------------------------------- 
$ Adding the value in AX and BX (the result is in CX):
$	STO IN1 DX
$	CC
$--------------------------------------------------
$ Subtracting the value in BX from AX (the result is in CX):
$	STO IN2 DX
$	CC
$--------------------------------------------------
$ 								   (if ZEROFLAG = 0 and carry = 0 then AX = BX  )
$ Comparing the value in AX and BX (if ZEROFLAG = 1 and carry = -1 then AX < BX )
$ 							 	   (if ZEROFLAG = 1 and carry = 0 then AX > BX	)
$	STO IN3 DX
$	CC
$--------------------------------------------------
$ Clearing all the registers, the ZEROFLAG and the carry value:
$	STO IN0 DX
$	CC
$--------------------------------------------------