    .global MAIN
    .ref q15exp

    .data
x:

    .word 0xc000
    .word 0x4d9f
    .word 0xffe1
    .word 0x7fe0
    .word 0xe539
    .word 0x67d3
    .word 0x2272
    .word 0x2783
    .word 0x2e44
    .word 0x37b7
    .word 0xac70
    .word 0x429d
    .word 0x1b5f
    .word 0x1e81
    .word 0xea8b
    .word 0x6c3c
    .word 0x71ae
    .word 0x3718
    .word 0x25b0
    .word 0x2bcf

result:
    .word 0x0000

    .text
MAIN:
	spm	1
    movw DP, #result
	movl XAR7, #x
    movw AR6, #10
    movw AR5, #0
test:
	movw AH, *XAR7++
	lcr q15exp
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
