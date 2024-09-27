method da400() returns(x:int)
requires true
ensures x== 400
{
    x:=400;
}


method suma3 (y: int) returns (x: int)
requires y + 3 %2 ==0
ensures x % 2 == 0
{
    x := y + 3;
}

method da65 (y: int) returns (x: int)
requires ( y < 65)
ensures y < x
{
    x := 65;
}

method  strange (x: int,y: int) returns (b: bool)
requires 
ensures b ==> x < y
{
    b := y < 10
    
}

