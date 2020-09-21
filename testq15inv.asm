    .global MAIN
    .ref q15inv

    .data
x:
    .word 0xc000
    .word 0x555f
    .word 0xfba6
    .word 0x7bc8
    .word 0xcec2
    .word 0x5c6d
    .word 0xaf7d
    .word 0x4f0a
    .word 0xe396
    .word 0x68bb
result:
    .word 0x0000

    .text
MAIN:
	spm	1
    movw DP, #result
	movl XAR7, #x
    movw AR6, #5
    movw AR5, #0
test:
	movw AH, *XAR7++
	lcr q15inv
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
