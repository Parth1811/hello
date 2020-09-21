    .global MAIN
    .ref q11mpy

    .data
x:
    .word 0x5030
    .word 0x72f0
    .word 0x4800
    .word 0x4140
    .word 0x4f00
    .word 0x2840
    .word 0x6de0
    .word 0xfc90
    .word 0xfd00
    .word 0x46f0
    .word 0x2f90
    .word 0x1a50
    .word 0x54f0
    .word 0x1900
    .word 0x1090
    .word 0x52c0
    .word 0x2500
    .word 0x17e0
    .word 0x1ef0
    .word 0x7360
    .word 0x1be0
    .word 0x4060
    .word 0x7e60
    .word 0x3f80
    .word 0x5fb0
    .word 0x3ea0
    .word 0x2ed0
    .word 0x6530
    .word 0x1630
    .word 0x1180
    .word 0x56b0
    .word 0x7770
    .word 0x50e0
    .word 0x4700
    .word 0xf930
    .word 0xfc30
    .word 0x0660
    .word 0x1a10
    .word 0x0140
    .word 0x2700
    .word 0x0460
    .word 0x0150
    .word 0x2dc0
    .word 0x2d70
    .word 0x1030
    .word 0x2140
    .word 0x4130
    .word 0x10e0
result:
    .word 0x0000

    .text
MAIN:
	spm	1
    movw DP, #result
	movl XAR7, #x
    movw AR6, #16
    movw AR5, #0
test:
	movw AH, *XAR7++
    movw AR0, AH
	movw AH, *XAR7++
    movw AR1, AH
	lcr q11mpy
	movw AL, *XAR7++
    movw AR0, AL
	movw AR1, AH
    movw AR5, AH
    BAR nextcase, AR1, AR0, EQ
	movw AH, #1
    movw T, AR6
    sub T, AH
    LSL AH, T
    ADD AH, @result
    movw @result, AH
nextcase:
    banz test, AR6--
spin:    lb	spin
	.end
