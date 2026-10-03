package com.example;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class AppTest {
    @Test
    void greetsTheProvidedName() {
        assertEquals("Hello, Ada!", App.greeting("Ada"));
    }
}
