package org.example;
import java.util.*;
import org.example.func.Func;
import org.example.func.Cat;
import org.example.func.Dog;
import org.example.func.Bird;


class Car {
    String name;
    int price;

    public Car(String name){
        this(name,0);
    }

    public Car(String name, int price){
        this.name = name;
        this.price = price;
    }
    public void start() {
        System.out.println(name + ": 출발");
    }

    public void howMuch() {
        System.out.println(name + ":" + price);
    }
}

class Ferrari extends Car {
    int price;
    public Ferrari(String name){
        super(name); // 부모 클래스 생성자 호출
    };

    public Ferrari(String name, int price){
        super(name);
        this.price = price;
    };

    public void getPrice() {
        System.out.println("price : " + price);
        System.out.println("this.price : " + this.price);
        System.out.println("super.price : " + super.price);
    }

    @Override
    public void start() {
        System.out.println(name + ": 페라리 출발");
    }

}


// 클래스
class Info {
    String name;
    String id;
    String pw;
    int age;
    // 생성자
    Info (String name, String id, String pw, int age){
        this.name = name;
        this.id = id;
        this.pw = pw;
        this.age = age;
    }
    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

}

public class Main {
    public static void main(String[] args) {
        Info info = new Info("정우진", "wj", "1234", 26);
        System.out.println(info.name);
        info.setName("김우진");
        System.out.println(info.name);
        String tmp = info.getName();
        System.out.println(tmp);

        // 오버로딩
        Func func = new Func(1,2,3);
        int x = func.add(1,2);
        System.out.println(x);
        int x2 = func.add(1,2,3);
        System.out.println(x2);

        // 생성자 오버로딩
        Car car1 = new Car("K5");
        Car car2 = new Car("K5", 5000);

        car1.howMuch();
        car2.howMuch();


        // 상속 및 오버라이딩
        Car ferrari1 = new Ferrari("페라리");
        Ferrari ferrari2 = new Ferrari("페라리2", 50000);

        //ferrari1.getPrice(); // 자식의 메소드는 사용불가
        ferrari2.getPrice(); // super로 부모 클래스 변수 상속 받기 가능

        car1.start();
        ferrari1.start(); // 오버라이딩

        // 추상 클래스 적용
        Cat cat = new Cat("고양이");
        Dog dog = new Dog("강아지");
        dog.bark();
        cat.bark();

        // 추상 클래스 + 인터페이스 적용
        Bird bird = new Bird("새");
        bird.bark();
        bird.fly();

        // try-catch
        int num = 5;
        int res;
        for (int i = 0; i<=num;i++) {
            try {
                res = num / i;
                System.out.println(res);
            } catch (Exception e) {
                System.out.println("exception: " + e.getMessage());
            } finally {
                System.out.println("항상 실행");
            }
        }
        // 리스트
        List list = new ArrayList(5);
        list.add(1);
        list.add("5");
        list.add("a");
        list.add("c");
        System.out.println(list);
        list.remove(3);
        System.out.println(list);
        System.out.println(list.size());
        for(int i = 0;i<list.size();i++){
            System.out.println(list.get(i));
        }
        for (Object cur:list) {
            System.out.println(cur);
        }
        // arraydeque
        ArrayDeque<Integer> ad = new ArrayDeque<>();
        ad.addFirst(1);
        ad.addFirst(2);
        ad.addLast(3);
        System.out.println(ad);
        ad.add(4); // 마지막 추가
        System.out.println(ad);
        ad.push(5);
        System.out.println(ad);

        //map

        Map<String, Integer> map = new HashMap<>();
        map.put("a",1); // put(k,v) 키값 쌍 추가
        map.put("a",2); // 키가 이미 존재하는 경우, 값 업데이트
        map.put("b",2);
        System.out.println(map.get("b")); // 키가 b인 value print
        System.out.println(map);

        Map<String, Integer> map2 = new HashMap<>();
        map2.put("c",3);
        map2.put("d",4):
        map.putAll(map2); // map2의 값들 모두 map에 추가
        System.out.println(map);
        map.remove(3);

        Set keyset = map.keySet();




    }
}
