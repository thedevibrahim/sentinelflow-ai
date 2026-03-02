package com.sentinelflow.controller;

import org.springframework.web.bind.annotation.*;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

import java.util.Map;

@RestController
@RequestMapping("/api")
public class SentimentController {

    private final WebClient webClient =
            WebClient.create("http://ai-model-service:5000");

    @PostMapping("/analyze")
    public Mono<Map> analyze(@RequestBody Map<String, String> body) {
        return webClient.post()
                .uri("/predict")
                .bodyValue(body)
                .retrieve()
                .bodyToMono(Map.class);
    }
}