package beatProgramming.BetData;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

/**
 * Clase que busca la informacion necesaria sobre los partidos y las ligas.
 *
 */
public class Getter {
	private WebDriver driver;

	public Getter() {
		driver = new FirefoxDriver();
	}

	/**
	 * Obtiene los partidos de una jornada en una determinada liga.
	 * 
	 * @param liga
	 * @param jornada
	 */
	public void getMatches(Liga liga, int jornada) {
		driver.get(generatePath(liga.getPath()) + jornada);
		WebElement col_resultados = driver.findElement(By.id("col-resultados"));
		for (WebElement partido : col_resultados.findElements(By
				.className("vevent"))) {
			String equipo1 = partido.findElement(By.className("equipo1"))
					.findElements(By.tagName("a")).get(1).getText();
			String equipo2 = partido.findElement(By.className("equipo2"))
					.findElements(By.tagName("a")).get(1).getText();
			String resultado = partido.findElement(By.className("rstd"))
					.findElement(By.className("clase")).getText();
			String[] goles_temp = resultado.split("-");
			int goles1 = Integer.parseInt(goles_temp[0]);
			int goles2 = Integer.parseInt(goles_temp[1]);
			System.out.println(equipo1 + " " + goles1 + " - " + goles2 + " "
					+ equipo2);
		}
	}

	public String generatePath(String path) {
		return "http://www.resultados-futbol.com" + path + "/grupo1/jornada";
	}

	public void prueba() {
		driver.get("http://www.resultados-futbol.com");
		System.out.println("Page title is: " + driver.getTitle());
	}

	public void close() {
		driver.quit();
	}
}
