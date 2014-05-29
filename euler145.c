#include <stdio.h>

#define TRUE 1
#define FALSE 0


int reverseNumber(int n)
{
	int reverse = 0;
	while (n > 0)
	{
		reverse = reverse * 10 + (n % 10);
		n /= 10;
	}
	return reverse;
}

int isReversible(int n)
{
	if ((n % 10) == 0)
		return FALSE;

	int reverse = reverseNumber(n);

	int sum = n + reverse;

	// Consists of odd decimals?
	while (sum > 0)
	{
		if (((sum % 10) & 1) == 0)
			return FALSE;

		sum /= 10;
	}

	return TRUE;
}

int main(void)
{
	int test = 11;
	int count = 0;
	int limit = 1000000000;

	while(test < limit)
	{
		if (isReversible(test) == TRUE)
			count += 2;

		test += 2;
	}
	printf("%d\n", count);
	return 0;
}