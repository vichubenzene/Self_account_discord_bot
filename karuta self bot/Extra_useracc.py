        message = await client.wait_for('message', check=check, timeout=30)
        a=random.randint(1,3)
        await asyncio.sleep(5)
        if a ==1 :
            await message.add_reaction("1️⃣")
        elif a==2:
            await message.add_reaction("3️⃣")
        else:
            await message.add_reaction("2️⃣")
        
    except:
        pass
