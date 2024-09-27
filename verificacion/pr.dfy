method pr(x:int,y:int)returns (suma:int)
requires x==10 && y < 50 
ensures suma <= 100
{
suma:= x+y;
} 