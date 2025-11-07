// Online C compiler to run C program online
#include <stdio.h>
#include <string.h>
void loopOne(){
    for(int i = 1 ; i <=5 ; i++){
      printf("%d \n" ,i);
    
    
}
  void looTwo(){
      
     for (int a = 1 ; a <=5 a ++){
         char row[50] = "";
         for(int b = 1  ; b <= 5 ; b++){
             char str[50] = "" ;
             sprintf(str ,"%d" ,a );
             strcat(row ,str);
             strcat(row , "");
         }
         printf("%s \n" , row);
     }
  }
      
 
    


}

int main() {
    // Write C code here
    looTwo();
        return 0;
}
