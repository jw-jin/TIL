package org.example.func;

public class Bird extends Animal implements Flyable {

    public Bird(String name) {
        super(name);
    }

    @Override
    public void fly() {
        System.out.println("날아감");
    }

    @Override
    public void bark() {
        System.out.println("짹짹");
    }
}
