# Sample Java Project

A small Java 17 command-line application built with Maven. It prints a greeting and includes a JUnit 5 test.

## Build and test

```bash
mvn test
mvn package
```

## Run

```bash
java -jar target/sample-java-project-1.0.0.jar Ada Lovelace
```

With no arguments, the app greets `World`.

## Run with Docker

```bash
docker build -t sample-java-project .
docker run --rm sample-java-project Ada Lovelace
```
