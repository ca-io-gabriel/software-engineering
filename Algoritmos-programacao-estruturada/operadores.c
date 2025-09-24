#include <stdio.h>

int main(){
	int tv2020, tv2021, tv2022;
	int note2020, note2021, note2022;
	int phone2020, phone2021, phone2022;

	tv2020 = 800;
	tv2021 = 950;
	tv2022 = 725;

	note2020 = 650; 
	note2020 = 550; 
	note2020 = 700; 

	phone2020 = 1500;
	phone2021 = 1800;
	phone2022 = 2100;

	printf("A media de 2020 e: %d\n", ((tv2020 + note2020 + phone2020) / 3));
	printf("A media de 2021 e: %d\n", ((tv2021 + note2021 + phone2021) / 3));
	printf("A media de 2022 e: %d\n", ((tv2022 + note2022 + phone2022) / 3));

	return 0;
}