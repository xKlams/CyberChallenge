<int check_flag(char *flag, size_t len)>:
 60d:	55                   	push   %ebp
 60e:	89 e5                	mov    %esp,%ebp
 610:	83 ec 40             	sub    $0x40,%esp
 613:	c6 45 cb 63          	movb   $0x63,-0x35(%ebp)
 617:	c6 45 cc 62          	movb   $0x62,-0x34(%ebp)
 61b:	c6 45 cd 6b          	movb   $0x6b,-0x33(%ebp)
 61f:	c6 45 ce 77          	movb   $0x77,-0x32(%ebp)
 623:	c6 45 cf 7f          	movb   $0x7f,-0x31(%ebp)
 627:	c6 45 d0 62          	movb   $0x62,-0x30(%ebp)
 62b:	c6 45 d1 69          	movb   $0x69,-0x2f(%ebp)
 62f:	c6 45 d2 68          	movb   $0x68,-0x2e(%ebp)
 633:	c6 45 d3 6c          	movb   $0x6c,-0x2d(%ebp)
 637:	c6 45 d4 56          	movb   $0x56,-0x2c(%ebp)
 63b:	c6 45 d5 60          	movb   $0x60,-0x2b(%ebp)
 63f:	c6 45 d6 3b          	movb   $0x3b,-0x2a(%ebp)
 643:	c6 45 d7 6e          	movb   $0x6e,-0x29(%ebp)
 647:	c6 45 d8 52          	movb   $0x52,-0x28(%ebp)
 64b:	c6 45 d9 61          	movb   $0x61,-0x27(%ebp)
 64f:	c6 45 da 61          	movb   $0x61,-0x26(%ebp)
 653:	c6 45 db 4f          	movb   $0x4f,-0x25(%ebp)
 657:	c6 45 dc 68          	movb   $0x68,-0x24(%ebp)
 65b:	c6 45 dd 7d          	movb   $0x7d,-0x23(%ebp)
 65f:	c6 45 de 66          	movb   $0x66,-0x22(%ebp)
 663:	c6 45 df 66          	movb   $0x66,-0x21(%ebp)
 667:	c6 45 e0 4a          	movb   $0x4a,-0x20(%ebp)
 66b:	c6 45 e1 70          	movb   $0x70,-0x1f(%ebp)
 66f:	c6 45 e2 7e          	movb   $0x7e,-0x1e(%ebp)
 673:	c6 45 e3 6a          	movb   $0x6a,-0x1d(%ebp)
 677:	c6 45 e4 6a          	movb   $0x6a,-0x1c(%ebp)
 67b:	c6 45 e5 6e          	movb   $0x6e,-0x1b(%ebp)
 67f:	c6 45 e6 44          	movb   $0x44,-0x1a(%ebp)
 683:	c6 45 e7 7f          	movb   $0x7f,-0x19(%ebp)
 687:	c6 45 e8 6f          	movb   $0x6f,-0x18(%ebp)
 68b:	c6 45 e9 2a          	movb   $0x2a,-0x17(%ebp)
 68f:	c6 45 ea 7c          	movb   $0x7c,-0x16(%ebp)
 693:	c6 45 eb 4b          	movb   $0x4b,-0x15(%ebp)
 697:	c6 45 ec 4c          	movb   $0x4c,-0x14(%ebp)
 69b:	c6 45 ed 11          	movb   $0x11,-0x13(%ebp)
 69f:	c6 45 ee 7c          	movb   $0x7c,-0x12(%ebp)
 6a3:	c6 45 ef 53          	movb   $0x53,-0x11(%ebp)
 6a7:	c6 45 f0 44          	movb   $0x44,-0x10(%ebp)
 6ab:	c6 45 f1 55          	movb   $0x55,-0xf(%ebp)
 6af:	c6 45 f2 78          	movb   $0x78,-0xe(%ebp)
 6b3:	c6 45 f3 41          	movb   $0x41,-0xd(%ebp)
 6b7:	c6 45 f4 5d          	movb   $0x5d,-0xc(%ebp)
 6bb:	c6 45 f5 75          	movb   $0x75,-0xb(%ebp)
 6bf:	c6 45 f6 43          	movb   $0x43,-0xa(%ebp)
 6c3:	c6 45 f7 4d          	movb   $0x4d,-0x9(%ebp)
 6c7:	c6 45 f8 5f          	movb   $0x5f,-0x8(%ebp)
 6cb:	c6 45 f9 4a          	movb   $0x4a,-0x7(%ebp)
 6cf:	c6 45 fa 52          	movb   $0x52,-0x6(%ebp)
 6d3:	83 7d 0c 30          	cmpl   $0x30,0xc(%ebp)
 6d7:	74 07                	je     6e0 <check_flag+0xd3>    // salta se len = 6
 6d9:	b8 00 00 00 00       	mov    $0x0,%eax
 6de:	eb 44                	jmp    724 <check_flag+0x117>
 6e0:	c7 45 fc 01 00 00 00 	movl   $0x1,var1          		// primo salto, var1 = 1
 6e7:	eb 2e                	jmp    717 <check_flag+0x10a>   // salta a salto 2
 6e9:	8b 55 fc             	mov    var1,%edx          		// salto 3, D = var1
 6ec:	8b 45 08             	mov    0x8(%ebp),%eax           // A = flag pointer
 6ef:	01 d0                	add    %edx,%eax                // A + var1  --    A + 2
 6f1:	0f b6 10             	movzbl (%eax),%edx              // edx = *flag
 6f4:	8b 45 fc             	mov    var1,%eax         		// eax = var1
 6f7:	31 d0                	xor    %edx,%eax                // xor edx, var1
 6f9:	88 45 fb             	mov    %al,-0x5(%ebp)           // mettiamo il primo byte di A in -5ebp
 6fc:	8d 55 cb             	lea    -0x35(%ebp),%edx         // edx = ptr 0x35
 6ff:	8b 45 fc             	mov    var1,%eax        		// eax = var1
 702:	01 d0                	add    %edx,%eax                // eax + edx (eax + var1) (eax + 2)
 704:	0f b6 00             	movzbl (%eax),%eax              // deferenziamo il
 707:	38 45 fb             	cmp    %al,-0x5(%ebp)           // compariamo al con il primo byte di A
 70a:	74 07                	je     713 <check_flag+0x106>   // se è tutto ok saltiamo a 713 per fare il check
 70c:	b8 00 00 00 00       	mov    $0x0,%eax
 711:	eb 11                	jmp    724 <check_flag+0x117>
 713:	83 45 fc 01          	addl   $0x1,var1 		        // aggiungiamo 1 alla variabile locale
 717:	8b 45 fc             	mov    var1,%eax  		        // salto 2, A = var1 (ora uguale a 2)
 71a:	39 45 0c             	cmp    %eax,0xc(%ebp)           // salta se len - var1 > 0
 71d:	77 ca                	ja     6e9 <check_flag+0xdc>    // salta a 3
 71f:	b8 01 00 00 00       	mov    $0x1,%eax
 724:	c9                   	leave  
 725:	c3                   	ret    
