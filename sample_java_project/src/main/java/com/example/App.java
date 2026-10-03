package com.example;

public class App {
    public static String greeting(String name) {
        return "Hello, " + name + "!";
    }

    public static void main(String[] args) {
        String name = args.length == 0 ? "World" : String.join(" ", args);
        System.out.println(greeting(name));
    }
}
