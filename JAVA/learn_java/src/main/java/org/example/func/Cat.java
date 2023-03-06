package org.example.func;

public class Cat extends Animal{

    public Cat(String name) {
        super(name);
    }

    @Override
    public void bark() {
        System.out.println(name + "야옹");
    }
}
