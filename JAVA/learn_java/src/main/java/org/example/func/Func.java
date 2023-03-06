package org.example.func;

public class Func {
    public int x,y,z;

    // 다른 패키지에서 접근하기 위해 접근제어자 public 선언
    public Func(int x, int y, int z){
        this.x = x;
        this.y = y;
        this.z = z;
    }

    // 메소드 오버로딩
    public int add(int x,int y){
        return x+y;
    }

    public int add(int x,int y, int z) {
        return x+y+z;
    }

}
