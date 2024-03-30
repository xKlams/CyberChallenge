#include <stdio.h>
#include <string.h>
#include <openssl/md5.h>

int main()
{
// 	unsigned char s1[] =
// {
//   212, 232, 167, 254, 232, 242, 160, 245, 226, 167, 
//   224, 232, 232, 227, 167, 230, 243, 167, 243, 239, 
//   238, 244, 167, 216, 197,   0
// };
// 	int esa_to_int = 173;
// 	for (int i = 0; i < strlen(s1); i++)
// 	{
// 		s1[i] ^= esa_to_int;
// 	}
// 	memfrob(s1, strlen(s1) - 2);
// 	printf("%s", s1);


	char s2[32];
	const unsigned char *s = (unsigned char *)"B";
	mbedtls_md5_ret(s, 1, s2);
	for (int i = 0; i < 16; i++)
	{
		printf("%02x", s2[i]);
	}
}
