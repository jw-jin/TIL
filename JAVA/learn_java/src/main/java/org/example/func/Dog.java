package org.example.func;

public class Dog extends Animal{

    public Dog(String name) {
        super(name);
    }

    @Override
    public void bark() {
        System.out.println(name + "멍멍");
    }
}
