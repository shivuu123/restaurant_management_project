def calculate_average_rating(reviews_queryset):
    try:
        total_reviews = reviews_queryset.count()
        if total_reviews == 0:
            return 0.0

        total_rating = sum(review.rating for review in reviews_queryset)
        average = total_rating / total_reviews
        return round(average, 2)

    except Exception as e:
        print(f"Error calculating average rating: {e}")
        return 0.0