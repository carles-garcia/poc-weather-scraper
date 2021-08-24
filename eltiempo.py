import typer

from services import WeatherForecast

app = typer.Typer()


@app.command()
def average_max(city: str):
    temp = WeatherForecast().get_average_max(city)
    if temp is not None:
        print(f"Week average max temperature for {city}: {temp: .1f} ºC")
    else:
        print(f"{city} not found")


@app.command()
def average_min(city: str):
    temp = WeatherForecast().get_average_min(city)
    if temp is not None:
        print(f"Week average min temperature for {city}: {temp: .1f} ºC")
    else:
        print(f"{city} not found")


if __name__ == "__main__":
    app()
