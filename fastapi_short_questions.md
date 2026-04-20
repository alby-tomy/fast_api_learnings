# FastAPI Short Questions & Answers

## Core Questions

### Q2
**What explains PUT idempotency vs PATCH?**  
Answer: PUT is idempotent; PATCH may not be.

### Q3
**How to return 404 if user not found?**  
Answer: Raise HTTPException(404).

### Q4
**Return JSON in FastAPI?**  
Answer: return {"Hello": "World"}

### Q5
**Handle expired JWT?**  
Answer: Catch ExpiredSignatureError using try-except.

### Q6
**OAuth2 login best approach?**  
Answer: Use OAuth2PasswordRequestForm.

### Q7
**Restrict query param using Enum?**  
Answer: Use Enum in type hint.

### Q8
**Multiple query params as list?**  
Answer: Use List[str].

### Q9/Q10
**Efficient bulk insert?**  
Answer: session.bulk_save_objects()

### Q11
**Limit columns in query?**  
Answer: load_only()

### Q12
**Correct ORM model?**  
Answer: Use Base, __tablename__, id PK.

### Q13
**OAuth2 login dependency?**  
Answer: OAuth2PasswordRequestForm

### Q14
**Map Pydantic to ORM?**  
Answer: model.dict()

### Q15
**Admin-only route?**  
Answer: Depends + HTTPException(403)

### Q16
**Pagination metadata?**  
Answer: Custom response model

### Q17
**Document 404 in OpenAPI?**  
Answer: responses={404: {"model": Error}}

### Q18
**Multiple decorators?**  
Answer: Same function handles both methods

### Q19
**Pagination best practice?**  
Answer: Include in JSON body

### Q20
**Custom validation error?**  
Answer: raise HTTPException(400)

### Q21
**Lowercase email validator?**  
Answer: @validator with value.lower()

### Q22
**How FastAPI shows validation?**  
Answer: JSON Schema

### Q23
**Generate migration?**  
Answer: alembic revision --autogenerate

### Q24
**Immediate ORM update?**  
Answer: session.flush()

### Q25
**Log delete?**  
Answer: Inside DELETE route

### Q26
**Async I/O?**  
Answer: await

### Q27
**POST request model?**  
Answer: item: Item

### Q28
**Read/write DB separation?**  
Answer: Dependency-based DB selection

### Q29
**Role-based access?**  
Answer: Depends + role check

---

## Additional Practice Questions

### Q30
**What does Depends() do?**  
Answer: Dependency injection system.

### Q31
**Difference between Query and Path?**  
Answer: Query = optional params, Path = required URL params.

### Q32
**What is response_model?**  
Answer: Defines output schema.

### Q33
**How to handle DB session lifecycle?**  
Answer: Use dependency with yield.

### Q34
**Difference between sync and async routes?**  
Answer: async supports non-blocking I/O.

### Q35
**How to secure routes?**  
Answer: OAuth2 + JWT + Depends.

### Q36
**What is middleware?**  
Answer: Runs before/after request.

### Q37
**What is Pydantic BaseModel?**  
Answer: Data validation & serialization.

### Q38
**How to handle file uploads?**  
Answer: UploadFile + File()

### Q39
**How to return custom status code?**  
Answer: Use status parameter or HTTPException.

---

## Quick Revision Tips

- Depends = power feature
- Pydantic = validation
- HTTPException = errors
- await = async
- bulk_save_objects = performance
