package beatProgramming.BetData;

import org.junit.Before;
import org.junit.Ignore;
import org.junit.Test;

public class GetterTest {

	private Getter getter;
	
	@Before
	public void setUp() {
		getter = new Getter();
	}
	
	/**
	 * Obtener partidos de una liga en una determinada jornada.
	 */
	@Test
	public void getMatches() {
		getter.getMatches(Liga.BBVA, 23);
	}
	
	@Test
	@Ignore
	public void prueba() {
		getter.prueba();
	}

}
