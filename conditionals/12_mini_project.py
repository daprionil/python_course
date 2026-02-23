# Proyecto

# Instrucciones:
# Crearás un programa de evaluación de candidatos potenciales con conocimientos en Python para RH.
# Obtendrás el nombre, años de experiencia y habilidades.

# Evaluarás:
# * Si el candidato sabe Python/Django, tiene +3 años de experiencia: Candidato Optimo.
# * Si el candidato sabe Python/Django, tiene +1 año de experiencia : Buen candidato.
# * Si el candidato sabe Python/Django: Posible candidato
# * Si el candidato no sabe Python: No optimo, se guardará CV

# Consejo: Ocupa los metodos .split()


class Candidate:
    name: str
    exp: int
    summary: str

    def __init__(self, name: str, exp: int, summary: str) -> None:
        self.name = name
        self.exp = exp
        self.summary = summary

    def validate_habilite(self, habilites: str | list[str] = "") -> bool:
        # Valida que la habilite se encuentre dentro del listado
        summary_candidate = self.summary.lower()
        if isinstance(habilites, list):
            is_valid = True

            # Valida por cada habilidad
            for hab in habilites:
                is_valid = hab.lower() in summary_candidate
                # Si no está en el summary, entonces corta el ciclo
                if not is_valid:
                    break

            return is_valid

        return habilites.lower() in summary_candidate

    def validate_experience(self, exp: int) -> bool:
        # Valida que esté en el rango
        return (self.exp - exp) >= 0


class ValidationCandidates:
    candidates: list[Candidate]

    def __init__(self, candidates: list[Candidate]) -> None:
        self.candidates = candidates

    def evaluate_candidates(self):
        for candidate in self.candidates:
            has_necessary_habilites = candidate.validate_habilite(
                "python"
            ) or candidate.validate_habilite("django")

            if candidate.validate_experience(3) and has_necessary_habilites:
                print(f"{candidate.name} es un Candidato óptimo")
            elif candidate.validate_experience(1) and has_necessary_habilites:
                print(f"{candidate.name} es un buen Candidato")
            elif has_necessary_habilites:
                print(f"{candidate.name} es un posible Candidato")
            else:
                print(f"{candidate.name} no es un Candidato óptimo, se guardará CV")


# CASO 1: Candidato Óptimo (Python/Django + más de 3 años de experiencia)
candidato_1 = Candidate(
    name="Laura Benítez",
    exp=5,
    summary="Desarrolladora backend con 5 años de experiencia en Python y Django. Especialista en Django REST Framework, optimización de consultas y despliegue en producción. Líder técnica en proyectos de alto tráfico.",
)

# CASO 2: Buen Candidato (Python/Django + más de 1 año de experiencia)
candidato_2 = Candidate(
    name="Carlos Mendoza",
    exp=2,
    summary="Desarrollador Python con 2 años de experiencia usando Django para desarrollo web. Participación en proyectos comerciales con Django ORM, autenticación y creación de APIs. Conocimientos sólidos del framework.",
)

# CASO 3: Posible Candidato (Sabe Python/Django, sin experiencia específica en años)
candidato_3 = Candidate(
    name="Valeria Soto",
    exp=0,
    summary="Graduada en bootcamp de programación con énfasis en Python y Django. Proyectos personales desarrollados con Django, incluyendo tienda virtual y blog. Entusiasta del desarrollo web y con muchas ganas de aprender.",
)

# CASO 4: No óptimo (No sabe Python, se guardará CV)
candidato_4 = Candidate(
    name="Ricardo Paz",
    exp=6,
    summary="Desarrollador Java con 6 años de experiencia en Spring Boot y microservicios. Experto en aplicaciones empresariales, bases de datos relacionales y arquitectura de software. Buscando nuevos desafíos.",
)

candidates = [candidato_1, candidato_2, candidato_3, candidato_4]
validation_candidates = ValidationCandidates(candidates)
validation_candidates.evaluate_candidates()
