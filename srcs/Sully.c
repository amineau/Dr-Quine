#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int i = 5;
#define Q(x)char*s=#x;x
Q(int main(){FILE *f;char *x_file;char *c_file;char *output;if(!strstr(__FILE__,"Sully.c")){i--;}if(i>=0){asprintf(&x_file,"Sully_%d",i);asprintf(&c_file,"Sully_%d.c",i);if(!(f=fopen(c_file,"w"))){return(0);}asprintf(&output,"gcc -Wall -Wextra -Werror -o %1$s %2$s && ./%1$s",x_file,c_file);fprintf(f,"#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\nint i = %d;\n#define Q(x)char*s=#x;x\nQ(%s)",i,s);fclose(f);system(output);}return(0);})